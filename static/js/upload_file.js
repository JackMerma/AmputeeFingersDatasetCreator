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

/*
function uploadFiles(){
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

    uploadForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const formData = new FormData(uploadForm);
	fetch('/upload', {
	    method: 'POST',
	    body: formData
	})
	    .then(response => response.json())
	    .then(data => {
		alert(data.message);
	    })
	    .catch(error => {
		console.error('Error:', error);
	    });
    });
}
*/
