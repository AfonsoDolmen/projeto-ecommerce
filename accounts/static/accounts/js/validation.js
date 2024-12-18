document.addEventListener('DOMContentLoaded', function(){
    const emailField = this.getElementById('email-field');
    const passwordField = this.getElementById('password-field')
    const confirmPasswordField = this.getElementById('confirm-password-field');

    // Validação email
    emailField.addEventListener('input', function(){
        const emailValue = emailField.value

        if (!emailValue.includes("@") || !emailValue.includes(".")) {
            emailField.classList.add('validation-error');
            emailField.placeholder = "Email inválido!";
        }else if (emailValue.lenght == 0) {
            emailField.placeholder = "Digite seu email";
        } else {
            emailField.classList.add('validation-success');
        }
    });

    // Validação senha
    passwordField.addEventListener('input', function(){
        const passwordLen = passwordField.value.length

        if (passwordLen < 8) {
            passwordField.classList.add('validation-error');
            passwordField.placeholder = "A senha deve conter no minimo 8 caracteres";
        } else if (passwordLen == 0) {
            passwordField.placeholder = "Digite sua senha";
        } else {
            passwordField.classList.add('validation-success');
        }
    });

    // Validação confirmação senha
    confirmPasswordField.addEventListener('input', function(){
        const confirmPasswordValue = confirmPasswordField.value
        const passwordValue = passwordField.value

        if (passwordValue != confirmPasswordValue) {
            confirmPasswordField.classList.add('validation-error');

            confirmPasswordField.placeholder = "As senhas devem ser as mesmas!";
        } else {
            confirmPasswordField.classList.add('validation-success');
        }
    });
});