function formValidate(form) {
    if (form.series_title.value === "") {
        alert("Series title is empty!");
        form.series_title.focus();
        return false;
    }
    if (form.issue_number.value === "") {
        alert("Issue number is empty!");
        form.issue_number.focus();
        return false;
    }
    if (form.issue_title.value === "") {
        alert("Issue title is empty!");
        form.issue_title.focus();
        return false;
    }
    if (form.month.value === "") {
        alert("Month is empty!");
        form.month.focus();
        return false;
    }
    if (form.writer.value === "") {
        alert("Writer is empty!");
        form.writer.focus();
        return false;
    }
    return true;
}