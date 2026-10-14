const songs = [
    "Author - Song Name",
];

const button = document.getElementById("us_button");
const user_input = document.getElementById("user_value");
const result = document.getElementById("result");

button.addEventListener("click", () => {
  const searchText = user_input.value;

  const song_index = songs.findIndex(song => song.includes(searchText));

   if (song_index === -1) {
     result.textContent = "Not found in this row";
   } else {
     result.textContent = `Songs "${songs[song_index]}" found in №${song_index + 1}`;
   }
});