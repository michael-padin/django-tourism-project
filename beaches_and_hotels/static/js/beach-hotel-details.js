let id;
const choiceImage = document.getElementById("beach-hotel-image");
const choiceTitle = document.querySelector(".choice-title");

const btnReserve = document.querySelector(".btn-reserve");
const booksWrapper = document.querySelector(".books__wrapper");
const reservationForm = document.getElementById("reservation-form");
const custDetailsWrapper = document.querySelector(".customer__details-wrapper");
const closeBtn = document.querySelector(".close-container");
const roomsSelect = document.getElementById("rooms");

const feedbackWrapper = document.querySelector(".feedback__wrapper");
const feedbackContainer = document.querySelector(".feedback__container");
const closeFeedbackBtn = document.querySelector(".close-feedback-container");

async function handleReservationSubmit(event) {
	event.preventDefault(); // Prevent form submission
	// Perform actions or send AJAX request based on the form data
	const formData = new FormData(event.target);
	// Example: Log the form data to the console
	const name = formData.get("name");
	const email = formData.get("email");
	const check_in_date = formData.get("check_in_date");
	const check_out_date = formData.get("check_out_date");
	const number_of_guests = formData.get("num_of_guests");
	const beach = parseInt(id);
	const hotel = parseInt(id);
	const room_type = parseInt(roomsSelect?.value) || null;
	// You can use JavaScript to further process the form data or send it to the server
	// using AJAX for asynchronous form submission
	// Example: Send form data to the server using AJAX

	const data = {
		room_type,
		number_of_guests,
		name,
		email,
		check_in_date,
		check_out_date,
		beach,
		hotel,
	};

	try {
		const response = await fetch(`/reservation/${id}/`, {
			method: "POST",
			body: JSON.stringify(data),
			headers: {
				"X-CSRFToken": "{{ csrf_token }}",
			},
		});
		if (response.ok) {
			const data = await response.json();
			reservationForm.reset();
			closeReservationForm();
			displayReservationFeedback();
		} else {
			console.error("Failed to submit reservation form.");
			alert("Failed to submit reservation form.");
		}
	} catch (error) {
		console.error("An error occurred:", error);
	}
}

async function fetchHotelBeachDetails(id) {
	try {
		const response = await fetch(`/hotel-beach-details-json/${parseInt(id)}/`);
		const data = await response.json();

		if (data.error) {
			alert("Something wen wrong while getting item info");
		} else {
			const imgUrl = data.beach.image_data;
			const name = data.beach.name;

			choiceImage.src = `data:image/jpeg;base64,${imgUrl}`;
			choiceTitle.textContent = name;
		}
	} catch (error) {
		// Handle any errors
		console.error(error);
	}
}

/** THIS FUNCTION WILL DISPLAY THE RESERVATION FORM */
function displayReservationForm(e) {
	id = e.target.getAttribute("data-id");

	fetchHotelBeachDetails(id);
	showLoader();
	setTimeout(() => {
		hideLoader();
		reservationForm.parentElement.classList.remove("popout");
		reservationForm.parentElement.classList.add("popup");
		custDetailsWrapper.classList.add("show");
	}, 500);
}

/**
 * THIS IS THE CLOSE ICON CONTAINER, IF THE ICON OR THE CONTAINER
 * IS CLICK THIS FEEDBACK FORM WILL CLOSE
 *  */
function closeFeedbackMessage() {
	feedbackContainer.classList.add("popout");
	setTimeout(() => {
		feedbackWrapper.classList.remove("show__feedback");
	}, 100);
}

/** THIS FUNCTION OR METHOD WILL CLOSE THE RESERVATION FORM  */
function closeReservationForm() {
	reservationForm.parentElement.classList.add("popout");
	setTimeout(() => {
		custDetailsWrapper.classList.remove("show");
	}, 100);
}

/**
 * THIS FUNCTION WILL OPEN/DISPLAY THE RESERVATION FEEDBACK
 * MESSAGE THIS MESSAGE WILL DISPLAY AFTER SUBMITTING
 * RESERVATION FORM
 */
function displayReservationFeedback() {
	feedbackContainer.classList.add("popup");
	feedbackWrapper.classList.add("show__feedback");
}

function showLoader() {
	const loader = document.createElement("div");
	loader.className = "loader-container";
	loader.innerHTML = `
      <div class="lds-roller">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    `;

	document.body.appendChild(loader);
}

function hideLoader() {
	const loader = document.querySelector(".loader-container");

	if (loader?.parentElement) {
		loader.parentNode.removeChild(loader);
	}
}

/* IF RESERVE BUTTON IS CLICK SHOW THE RESERVATION FORM */
btnReserve.addEventListener("click", displayReservationForm);

if (closeFeedbackBtn)
	closeFeedbackBtn.addEventListener("click", closeFeedbackMessage);
closeBtn.addEventListener("click", closeReservationForm);
document
	.getElementById("reservation-form")
	.addEventListener("submit", handleReservationSubmit);
