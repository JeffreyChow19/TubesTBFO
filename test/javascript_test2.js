const question_bar = document.getElementById('question-bar');
const start_button = document.getElementById("start-button");
const start_prompt = document.querySelector(".start-prompt");
const restart_button = document.getElementById('restart-button');
const result_prompt = document.querySelector('.result-prompt');
let result_bar = document.getElementById('result-bar');
const prog_bar = document.querySelector(".prog-bar");
const outer_bg = document.querySelector(".outer-background");
const outer_bg_contents = document.querySelector('.outer-background-contents');
const result_arr = ['Happy' , 'Neutral' , 'Sad'];

// for user history
var history_score = JSON.parse(localStorage.getItem("history_array"));
if (history_score == null){ history_score = []}; // catch if empty
const history_prompt = document.querySelector(".history-prompt");
const last_result_bar = document.getElementById("last-result-bar");
const all_result_bar = document.getElementById("all-result-bar");

// for user progress
let current_index = 0;
const red_button = document.getElementById("red");
const green_button = document.getElementById("green");
const arr_of_question = ['Was your morning any good?','Was today a good day?','Was there something good happened recently?','Have you achieved something big today?'
,'Is there something good happening tonight?','Do you want this day to not go past quickly?','Are you feeling happy right now?','Did you sleep well last night?','Do you feel being loved enough today?','Are you waiting for todays lunch?'];
let score = 0;
let current_progress = Number(document.getElementById("bar-fill").style.width); // element to change
const maxProgress = 10;

// user progress
function progress () {
    current_progress++; 
    document.getElementById("bar-fill").style.width = String(100*current_progress/maxProgress)+"%";
}

// reset animation for button and question if n of answered question < 10
function resetAnimation () {
    const question_bar_animation = document.getElementById("question-bar");
    const red_button_animation = document.getElementById("red");
    const green_button_animation = document.getElementById("green");
    red_button_animation.style.animation = "none";
    red_button_animation.offsetHeight;
    red_button_animation.style.animation = null;
    green_button_animation.style.animation = "none";
    green_button_animation.offsetHeight;
    green_button_animation.style.animation = null;
    question_bar_animation.style.animation = "none";
    question_bar_animation.offsetHeight;
    question_bar_animation.style.animation = null;
}

// calculating animation function
function pre_result_animation () {
    question_bar.classList.remove('question-bar');
    question_bar.classList.add('stop');
    question_bar.style.pointerEvents = "none";
    question_bar.innerHTML = "Calculating your results";
    outer_bg_contents.classList.add('spin');
    outer_bg_contents.style.position = "relative";
    outer_bg_contents.style.top = "1em";
    outer_bg_contents.style.pointerEvents = "none";
    outer_bg_contents.innerHTML = '<p>|</p>'
}


// result
function result (score, condition) {
    history_score.push(score);
    localStorage.setItem("history_array", JSON.stringify(history_score));
    setActive(result_prompt);
    setActive(outer_bg , condition);
    setActive(prog_bar, condition);
    if (score < 4) {
        result_bar.innerText = 'Current Mood: ' + result_arr[2];
    } 
    else {
        if (score < 8){
            result_bar.innerText = 'Current Mood: ' + result_arr[1];
        }
        else{
            result_bar.innerText = 'Current Mood: ' + result_arr[0];
        }
    }
}

function setActive (elmt, value = true) {
    if(value) {elmt.classList.remove("hidden"); elmt.style.pointerEvents = "initial";}
    else {elmt.classList.add("hidden"); elmt.style.pointerEvents = "none";}
}


// restart quiz + store historical score to local
function restart () {
    localStorage.setItem("history_array",JSON.stringify(history_score)); //moved it to result()
    location.reload();
}

// fetch historical score from local
const history_bar = document.getElementById('history-arr');
function get_history () {
    let string_array = localStorage.getItem("history_array");
    history_score = JSON.parse(string_array);

    document.querySelector(".history-prompt>div>span").innerHTML = history_score.length;

    let result_mean = result_total = 0;
    for (let i = 0; i<history_score.length;i++){
        result_total += history_score[i];
    }

    result_last = history_score[history_score.length-1].toFixed(3);
    result_mean = (result_total /= history_score.length).toFixed(3);

    last_result_bar.style.width = String(result_last) + "em";
    all_result_bar.style.width = String(result_mean) + "em";

    last_result_bar.innerHTML = result_last;
    all_result_bar.innerHTML = result_mean;

    setActive(history_prompt);
    
}