package com.example.loginunit3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.example.loginunit3.modelos.Usuario;

public class WelcomeActivity extends AppCompatActivity {

    private TextView welcometext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome);
        welcometext = findViewById(R.id.welcometext);
        initWelcome();
    }

    public void initWelcome(){
        final String Mensaje_Bienvenido = "Bienvenido ";
        final String Mensaje_Usuario = "Usuario: ";
        Bundle bundle = getIntent().getBundleExtra("bundle");
        Usuario usuario = (Usuario) bundle.getSerializable("usuario");
        if(usuario!=null){
            welcometext.setText(Mensaje_Usuario+usuario.getUser());
            Toast.makeText(this,
                    Mensaje_Bienvenido+usuario.getNombre(),
                    Toast.LENGTH_LONG).show();
        }
    }
}