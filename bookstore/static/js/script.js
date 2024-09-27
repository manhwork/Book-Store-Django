// show input filter 
const showFilter = document.querySelector(`span[show-filter]`);
if (showFilter) {
    showFilter.addEventListener('click', (e) => {
        const formFilter = document.querySelector(`form[form-filter]`);
        if (formFilter) {
            formFilter.classList.remove("d-none");
            formFilter.classList.add("d-block");
        }
    });
}
// end show input filter
