package com.example.loginunit3;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.example.loginunit3.modelos.Usuario;
import com.example.loginunit3.modelos.UsuarioBD;
import com.example.loginunit3.util.MensajeError;

public class MainActivity extends AppCompatActivity {

    private TextView tituloText;
    private EditText userText;
    private EditText passText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tituloText = findViewById(R.id.tituloText);
        userText = findViewById(R.id.userText);
        passText = findViewById(R.id.passText);
    }

    public  void validarEntrada(View view){
        UsuarioBD usuarioBD = new UsuarioBD();
        Usuario usuario = usuarioBD.login(userText.getText().toString(),
                passText.getText().toString());

        String mensaje = MensajeError.mostrarMensajeError(userText.getText().toString(),
                passText.getText().toString());

        if (mensaje.isEmpty()) {

            transaccionEntrada(usuario);
        } else {
            Toast.makeText(this,
                    mensaje,
                    Toast.LENGTH_LONG).show();
        }
    }

    public void transaccionEntrada(Usuario usuario){
        if (usuario == null) {
            Toast.makeText(this,
                    "Entrada Invalida Usuario o Password Incorrecto",
                    Toast.LENGTH_LONG).show();
        } else {
            entradaSistema(usuario);

        }

    }


    public void entradaSistema(Usuario usuario){
        usuario.setPassword("********************");
        Intent intent = new Intent(MainActivity.this, WelcomeActivity.class);
        Bundle bundle = new Bundle();
        bundle.putSerializable("usuario",usuario);
        intent.putExtra("bundle",bundle);
        startActivity(intent);
    }
}