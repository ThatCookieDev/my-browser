const searchInput = document.getElementById("search");

searchInput.addEventListener("keydown", function(event){
    if (event.key === "Enter") {
         let query = searchInput.value;
         window.location.href = "https://www.google.com/search?q=" + query;
    }
})