//Formulario de login
const form = document.getElementById("loginForm");

// Mensajes de error
const message = document.getElementById("message");

form.addEventListener("submit", async (e) => {

    //Con esto evitamos que se recargue la pagina
    e.preventDefault();

    //Obetenemos los datos del formulario
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {

        //leer usuarios del archivo json
        const response = await fetch("./users.json");
        const users = await response.json();

        console.log(users);

    } catch (error) {

        console.error(error);
    }

});