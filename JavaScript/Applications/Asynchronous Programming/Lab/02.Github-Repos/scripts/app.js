function loadRepos() {
	const usernameField = document.getElementById('username');
	const itemsList = document.getElementById('repos');

	const username = usernameField.value;
	const url = `https://api.github.com/users/${username}/repos`;

	itemsList.replaceChildren();

	fetch(url)
	.then((response) => {
		if(response.status != 200){
			let item = document.createElement("li"); 
			let err = document.createElement("h3"); 
			err.textContent = "No such user or repositories found!"; 
			itemsList.appendChild(item);
			item.append(err);
		}
	})
	.then((response) => response.json())
	.then((data) => {
		for(let r in data){ 
			let listItem = document.createElement("li");
			let repoLink = document.createElement("a");
			repoLink.setAttribute("href", data[r].html_url);
			
			itemsList.appendChild(listItem);
			listItem.appendChild(repoLink);
			repoLink.textContent = data[r].full_name;
		}
	})
	.catch((error) => error)
}