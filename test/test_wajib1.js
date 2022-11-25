// for user history
var history_score = JSON.parse(localStorage.getItem("history_array"));
if (history_score == null){ history_score = [];} // catch if empty
const history_prompt = document.querySelector(".history-prompt");
const last_result_bar = document.getElementById("last-result-bar");
const all_result_bar = document.getElementById("all-result-bar");