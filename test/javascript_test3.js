let title = document.getElementById('carousel-title'); 
let content = document.getElementById('carousel-content');
let img = document.getElementById('carousel-img');
// Toggle
let control_1 = document.getElementById('control-1');
let control_2 = document.getElementById('control-2');
let control_3 = document.getElementById('control-3');
let all_switch = [control_1, control_2, control_3];

// Looper
let current_index = 0;

function resetAnimation (element) {
    element.style.animation = "none";
    element.offsetHeight;
    element.style.animation = null;
}

function next (current_index) {
  title.innerHTML = carousel_title[current_index];
  title.classList.add('fade-in');
  resetAnimation(title);
  toggleSwitch(current_index);
  content.innerHTML = carousel_content[current_index];
  content.classList.add('fade-in');
  resetAnimation(content);
  img.setAttribute("src", carousel_img[current_index]);
  img.classList.add('fade-in');
  resetAnimation(img);

  // all_toggle[current_index].classList.add('active');
}


control_1.addEventListener('click', function name () {
    toggleSwitch(1);
    current_index = 0;
    next(current_index);
})
control_2.addEventListener('click', function name () {
toggleSwitch(2);
current_index = 1;
next(current_index);
})
control_3.addEventListener('click', function name () {
toggleSwitch(3);
current_index = 2;
next(current_index);
})