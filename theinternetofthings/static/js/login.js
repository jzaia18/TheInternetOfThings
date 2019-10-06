var swapper_l = document.getElementById("swapper-l");
var swapper_s = document.getElementById("swapper-s");

var login_tab = document.getElementById("login-tab");
var signup_tab = document.getElementById("signup-tab");

swapper_l.addEventListener("click", function()
                           { $("#login-tab").fadeOut(300, function()
                                                     { $("#signup-tab").fadeIn();}); });
swapper_s.addEventListener("click", function()
                           { $("#signup-tab").fadeOut(300, function()
                                                      { $("#login-tab").fadeIn(); }); });
