document.addEventListener("DOMContentLoaded", function() {
    const pathname = window.location.pathname;
    const selectCreate_by = document.querySelector('#create_bySelect');
    if (selectCreate_by) {
        selectCreate_by.addEventListener("change", function(e) {
            const params = e.target.value ? {"created_by": e.target.value} : {};
            const queryString = new URLSearchParams(params).toString();
            const url = queryString ? pathname + "?" + queryString : pathname;
            window.location.replace(url);
        })
    }
});