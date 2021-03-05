function addPost() {
  const form = document.getElementById("addP");
  const inputs = form.getElementsByTagName("input");
  let blog = {
    image: inputs[0].value,
    title: inputs[1].value,
    year: inputs[2].value,
    description: inputs[3].value,
  };

  console.log(blog);
  fetch("http://127.0.0.1:5000/addP/", {
    method: "POST",
    body: JSON.stringify(blog),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      alert("Post have been submitted");
      document.getElementById("addP").reset();
    });
}

function blogfetch() {
  fetch("http://127.0.0.1:5000/");
}
