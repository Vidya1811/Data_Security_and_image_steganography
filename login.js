function validate()
{
  var username=document.getElementById("username").Value;
  var username=document.getElementById("password").Value;
  if(username=="admin" && password=="user")
  {
    alert("login is succesful");
    return false;
  }
else
{
  alert("login failed");
}
}