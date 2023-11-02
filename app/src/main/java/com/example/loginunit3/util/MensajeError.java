package com.example.loginunit3.util;

public class MensajeError {

    public static String mostrarMensajeError(String user, String password){
        String errores = "";
        if(user.isEmpty()){
            errores += "* Campo Usuario Vacio\n";
        }
        if(password.isEmpty()){
            errores += "* Campo Password Vacio\n";
        }
        return errores.trim();
    }
}
