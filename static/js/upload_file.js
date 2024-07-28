function uploadFiles() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const uploadForm = document.getElementById('uploadForm');

    dropzone.addEventListener('click', () => {
	fileInput.click();
    });

    dropzone.addEventListener('dragover', (e) => {
	e.preventDefault();
	dropzone.classList.add('bg-light');
    });

    dropzone.addEventListener('dragleave', () => {
	dropzone.classList.remove('bg-light');
    });

    dropzone.addEventListener('drop', (e) => {
	e.preventDefault();
	dropzone.classList.remove('bg-light');
	fileInput.files = e.dataTransfer.files;
    });
}
