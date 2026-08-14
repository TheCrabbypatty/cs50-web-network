document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".edit-btn").forEach(button => {
        button.onclick = () => {
            const id = button.dataset.id;
            const post = document.querySelector(`#post-${id}`);
            const content = post.querySelector(".content");
            const old_content = content.innerText;
            content.innerHTML = `<textarea class = "edit-area">${old_content}</textarea> <br> <button class = "save-btn">Save</button>`
            button.style.display = "none";
            post.querySelector(".save-btn").onclick = () => {
                const newContent = post.querySelector(".edit-area").value;

                fetch(`/edit/${id}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ content: newContent })
                })
                .then(response => response.json())
                .then(data => {
                    content.innerText = data.content;
                    button.style.display = "inline-block";
                });
        };
    }});
});

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".like-btn").forEach(button => {
        button.onclick = () => {
            const id = button.dataset.id;

            fetch(`/like/${id}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                button.innerText = `Like (${data.likes})`;
            });
        };
    });
});