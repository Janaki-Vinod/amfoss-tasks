function saveLocalStorage(){
  if (typeof(Storage) !== "undefined") {
    localStorage.setItem("firstname", "Janaki");
    localStorage.setItem("lastname", "Vinod");
    alert('Data saved');
  } else {
      alert('Sorry');
  }
}
function currentTime(){
  var datetime = new Date().toLocaleString();
  alert(datetime);
}
function changeBackground(){
  document.body.style.background = 'red';
}
function refreshPage(){
  window.location.reload();
}
function newWindow(){
  var myWindow = window.open("", "Hello", "width=400,height400");
    myWindow.document.write("<p>Hello</p>");
}
function logConsole(){
  console.log('I did it');
}
