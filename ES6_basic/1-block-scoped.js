export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;
  console.log(task, task2);

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
    console.log(task, task2);
  }

  return [task, task2];
}
