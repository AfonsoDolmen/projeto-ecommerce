document.addEventListener('DOMContentLoaded', function(){
    const emailField = this.getElementById('email-field');
    const passwordField = this.getElementById('password-field')
    
    // Validação email
    emailField.addEventListener('input', function(){
        const emailValue = emailField.value

        if (!emailValue.includes("@")) {
            emailField.classList.add('validation-error');
            emailField.placeholder = "Email inválido!";
        } else {
            emailField.classList.add('validation-success');
        }
    });

    // Validação senha
    passwordField.addEventListener('input', function(){
        const passwordLen = passwordField.value.length

        if (passwordLen != 8) {
            passwordField.classList.add('validation-error');
            passwordField.placeholder = "A senha deve conter no minimo 8 caracteres";
        } else {
            passwordField.classList.add('validation-success');
        }
    });
});