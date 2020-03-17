// function validate_img(field, alerttxt) {
//     var fileInput = $('#file').get(0).files[0];
//     if (fileInput) {
//         return true
//     } else {
//         return false
//     }
//
// }

function validate_form(thisform) {
    with (thisform) {
        var fileInput = $('#file').get(0).files[0];
        if (fileInput) {
            return true
        } else {
            alert("Pleaase upload a photo")
            return false
        }
    }
}