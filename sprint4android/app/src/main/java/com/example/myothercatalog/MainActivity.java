package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Asigna recycler view al elemento del xml
        recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;

        // Crea con volley una peticion GET de un Json Array
        JsonArrayRequest request = new JsonArrayRequest(
                // Indica el tipo de peticion
                Request.Method.GET,
                // Indica la url a donde mandar la peticion
                "https://raw.githubusercontent.com/narCord/DAM/main/recursos/catalog.json",
                // El cuerpo de la peticion, que ira vacio
                null,
                // El response listener escuchara las respuestas validas del servidor
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<BookData> bookList = new ArrayList<>();
                        // Cuando reciba una respuesta parseara el Json recibido y lo almacenara en una lista
                        for(int i = 0; i < response.length(); i++){
                            try {
                                JSONObject jsonObject = response.getJSONObject(i);
                                BookData data = new BookData(jsonObject);
                                bookList.add(data);
                            } catch (JSONException e) {
                                throw new RuntimeException(e);
                            }
                        }
                        // Se instancia un nuevo adapter con la lista creada y la actividad actual como parametros
                        // La clase adapter creara una vista por cada item de la lista
                        BookRecyclerViewAdapter adapter = new BookRecyclerViewAdapter(bookList, activity);
                        // Se asigna al recycler view el adapter
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                }
        );
        // Se añade el JsonArrayRequest a la cola de peticiones
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }
}