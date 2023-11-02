package com.example.loginunit3.modelos;

import java.io.Serializable;

public class Usuario  implements Serializable {

    private String id;
    private String user;

    private String nombre;

    private String password;

    public Usuario(String id, String user, String nombre, String password) {
        this.id = id;
        this.user = user;
        this.nombre = nombre;
        this.password = password;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
