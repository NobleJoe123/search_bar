function toggleForm() {
    const form = document.getElementById('createForm');
    const button = document.getElementById('createButton');
    if (form.style.display === 'none') {
        form.style.display = 'block';
        button.textContent = 'Cancel';
        button.style.backgroundColor = 'red';
    } else {
        form.style.display = 'none';
        button.textContent = 'Create';
        button.style.backgroundColor = '#28a745';
    }
}





























































// document.addEventListener(function () {
//             const updateButtons = document.querySelectorAll('.update-btn');
//             const updateFormContainer = document.getElementById('update-form-container');
//             const updateForm = document.getElementById('update-form');
//             const cancelUpdateBtn = document.getElementById('cancel-update');

//             updateButtons.forEach(button => {
//                 button.addEventListener('click', function () {
//                     // Get product data from the button's data attributes
//                     const productId = this.getAttribute('data-id');
//                     const productName = this.getAttribute('data-name');
//                     const productDescription = this.getAttribute('data-description');
//                     const productPrice = this.getAttribute('data-price');

//                     // Fill the form with the product's current details
//                     document.getElementById('product-id').value = productId;
//                     document.getElementById('product-name').value = productName;
//                     document.getElementById('product-description').value = productDescription;
//                     document.getElementById('product-price').value = productPrice;

//                     // Set the form action to the update URL
//                     updateForm.action = `/update/${productId}/`;

//                     // Show the form
//                     updateFormContainer.classList.remove('hidden');
//                 });
//             });

//             // Hide the form when cancel is clicked
//             cancelUpdateBtn.addEventListener('click', function () {
//                 updateFormContainer.classList.add('hidden');
//             });
//         });