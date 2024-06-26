// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
// 	console.log("Content script received meaning:", request.meaning)
// 	if (request.meaning) {
// 		console.log("creating tooltip")
// 		const tooltip = document.createElement("div")
// 		tooltip.className = "meaning-tooltip"
// 		tooltip.innerText = request.meaning

// 		const selection = window.getSelection()
// 		if (selection.rangeCount > 0) {
// 			const range = selection.getRangeAt(0)
// 			const rect = range.getBoundingClientRect()
// 			tooltip.style.top = rect.top - tooltip.offsetHeight + "px"
// 			tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + "px"

// 			document.body.appendChild(tooltip)

// 			setTimeout(() => {
// 				document.body.removeChild(tooltip)
// 			}, 5000)
// 		}
// 	}
// })

document.addEventListener("mouseup", event => {
	if (event.target.tagName === "A") return

	const text = window.getSelection().toString()
	console.log("Selected text:", text)

	if (text) {
		chrome.runtime.sendMessage({ text }, response => {
			console.log("Content script sent message:", text)
			if (chrome.runtime.lastError) {
				console.error("Failed to send message:", chrome.runtime.lastError)
			} else {
				console.log("Content script received response:", response)
				if (response.meaning) {
					console.log("Received meaning:", response.meaning)

					const tooltip = document.createElement("div")
					tooltip.className = "meaning-tooltip"
					tooltip.innerText = response.meaning
					console.log("creating tooltipp")

					const selection = window.getSelection()
					if (selection.rangeCount > 0) {
						const range = selection.getRangeAt(0)
						const rect = range.getBoundingClientRect()
						tooltip.style.top = rect.top - tooltip.offsetHeight + "px"
						tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + "px"

						document.body.appendChild(tooltip)

						setTimeout(() => {
							document.body.removeChild(tooltip)
						}, 5000)
					}
				}
			}
		})
	}
})
