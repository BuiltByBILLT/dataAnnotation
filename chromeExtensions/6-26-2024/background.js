import { WORDSAPI_KEY } from "./config.js"
console.log("Background script started")

async function getMeaning(text) {
	try {
		console.log(`Fetching meaning for: ${text}`)
		const url = `https://wordsapiv1.p.rapidapi.com/words/${text}/definitions`

		const options = {
			method: "GET",
			headers: {
				"X-RapidAPI-Key": WORDSAPI_KEY,
				"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
			},
		}

		const response = await fetch(url, options)
		const data = await response.json()

		console.log("API response:", data)

		if (data.definitions && data.definitions.length > 0) {
			const definition = data.definitions[0].definition
			console.log("Definition found:", definition)
			return definition
		} else {
			console.log("Definition not found.")
			return "Definition not found."
		}
	} catch (error) {
		console.error("Error getting meaning:", error)
		return "Sorry, an error occurred while getting the definition. Please try again."
	}
}

chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
	if (request.text) {
		console.log("Received text:", request.text)
		const meaning = await getMeaning(request.text)
		console.log("Sending response:", meaning)
		sendResponse({ meaning })
	} else {
		sendResponse({ meaning: "No text provided." })
	}
	return true // Indicate response is async
})
