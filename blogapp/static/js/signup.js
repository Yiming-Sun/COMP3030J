function validate_img(field, alerttxt) {
    var fileInput = $('#file').get(0).files[0];
    if (fileInput) {
        return true
    } else {
        alert(alerttxt)
        return false
    }

}

function validate_form(thisform) {
    with (thisform) {
        if (validate_img(file, "Please upload a photo") == false) {
            email.focus();
            return false
        }
    }
}