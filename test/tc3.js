const sum = 10;
if (sum > 30) {
  if (sum > 25 && sum < 28) {
    console.log(1);
  } else {
    console.log(2);
  }
} else if (sum > 15) {
  if (sum > 18 && sum < 20) {
    console.log(3);
  } else if (sum > 20 && sum < 25) {
    console.log(4);
  }
} else if (sum > 5) {
  console.log(sum);
} else {
  console.log("failed...");
}
