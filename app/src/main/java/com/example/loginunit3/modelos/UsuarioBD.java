package com.example.loginunit3.modelos;

import java.util.List;
import java.util.ArrayList;

public class UsuarioBD {

    List<Usuario> usuarios = new ArrayList<>();

    public UsuarioBD(){
            bdUsuario();
    }

    private List<Usuario> bdUsuario(){
        usuarios.add(new Usuario("1","rene","rene cardona","123456"));
        usuarios.add(new Usuario("2","jose","jose herrera","123456"));
        return usuarios;
    }


    public Usuario login(String user,String password){
        Usuario usuarioEncontrado = null;
        for(Usuario usuario:usuarios){
            if(usuario.getUser().equals(user)  && usuario.getPassword().equals(password)){
                usuarioEncontrado = usuario;
                break;
            }
        }
        return usuarioEncontrado;
    }


}
