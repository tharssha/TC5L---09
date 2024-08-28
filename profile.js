document.getElementById('profile-picture').addEventListener('change', function() {
    const file = this.files[0];
    const previewImage = document.getElementById('preview-img');
    const previewText = document.getElementById('preview-text');

    if (file) {
        const reader = new FileReader();

        previewText.classList.add('hidden');
        previewImage.classList.remove('hidden');

        reader.addEventListener('load', function() {
            previewImage.setAttribute('src', this.result);
        });

        reader.readAsDataURL(file);
    } else {
        previewText.classList.remove('hidden');
        previewImage.classList.add('hidden');
        previewImage.setAttribute('src', '');
    }
});

document.getElementById('profile-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Profile saved successfully!');
    // Implement form submission handling here.
});