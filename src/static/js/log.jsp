<script language = "JavaScript">
    function validate() {
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        if (username == null || username == "") {
            alert("Please enter the username.");
            return false;
        }
        if (password == null || password == "") {
            session.setAttribute("errMsg", "로그인 정보가 올바르지 않습니다.");
            return false;
        }
        alert('Login successful');
        
    } 
</script>