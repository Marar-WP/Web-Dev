const taskForm = document.querySelector("#taskForm");
const taskInput = document.querySelector("#taskInput");
const taskList = document.querySelector("#taskList");
const filterButtons = document.querySelectorAll(".fb1");

let currentFilter = "all";

function applyFilter() {
  const items = taskList.querySelectorAll(".li1");

  items.forEach(item => {
    const isCompleted = item.classList.contains("completed");
    let shouldShow = true;

    if (currentFilter === "active") {
      shouldShow = !isCompleted;
    }

    if (currentFilter === "completed") {
      shouldShow = isCompleted;
    }

    item.classList.toggle("hidden", !shouldShow);
  });
}

function createTaskItem(text) {
  const li = document.createElement("li");
  li.className = "li1";

  const left = document.createElement("div");
  left.className = "l2";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  const span = document.createElement("span");
  span.className = "t2";
  span.innerText = text;

  const delBtn = document.createElement("button");
  delBtn.className = "b2";
  delBtn.innerText = "✖";

  checkbox.addEventListener("change", function () {
    span.classList.toggle("done");
    li.classList.toggle("completed", checkbox.checked);
    applyFilter();
  });

  delBtn.addEventListener("click", function () {
    taskList.removeChild(li);
    applyFilter();
  });

  left.appendChild(checkbox);
  left.appendChild(span);

  li.appendChild(left);
  li.appendChild(delBtn);

  return li;
}

taskForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const value = taskInput.value.trim();
  if (value === "") {
    alert("enter the value");
    return;
  }

  const task = createTaskItem(value);
  taskList.appendChild(task);

  taskInput.value = "";
  applyFilter();
});

filterButtons.forEach(btn => {
  btn.addEventListener("click", function () {
    currentFilter = btn.dataset.filter;

    filterButtons.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    applyFilter();
  });
});

