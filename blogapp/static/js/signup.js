

        function validate_name(field,alerttxt) {
                var user=field.value;
                var reg=/^[a-zA-Z][a-zA-Z0-9]{3,15}$/;
                if(!reg.test(user)){
                    alert(alerttxt);
                    return false;
                 }
                else{
                    return true;
                 }
        }

        function validate_email(field,alerttxt) {
                var email=field.value;
                var reg=/^\w+@\w+\.(com)$|(cn)$/;
                if(!reg.test( email)){
                    alert(alerttxt);
                    return false
                }
                else {
                    return true
                }

         }


        function validate_pass(field,alerttxt) {
                var pwd=field.value;
                var reg=/^[a-zA-Z0-9]{4,10}$/;
                if(!reg.test(pwd)){
                    alert(alerttxt);
                    return false;
                 }
                else{
                    return true;
                 }
        }



        function validate_form(thisform) {
            with (thisform) {
                if (validate_name(username, "User name consists of English letters and Numbers of 4 to 16 characters, begin with a letter")==false){
                    username.focus();
                    return false
                }if (validate_email(email,"Not a valid e-mail address!")==false){
                    email.focus();
                    return false
                }
            }
        }