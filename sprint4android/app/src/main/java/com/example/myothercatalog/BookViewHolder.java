package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class BookViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;
    private BookData book;

    // Al instanciarse asigna un TextView, un ImageView y un OnClickListener a una view
    public BookViewHolder(@NonNull View itemView) {
        super(itemView);

        textView = itemView.findViewById(R.id.book_text_view);
        imageView = itemView.findViewById(R.id.book_image_view);

        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Almacena los datos de book
                String bookName = book.getName();
                String bookImageUrl = book.getUrl();
                String bookDescription = book.getDescription();

                // Crea un nuevo intent de DetailActivity y carga los datos en el
                Context context = v.getContext();
                Intent intent = new Intent(context, DetailActivity.class);
                intent.putExtra(DetailActivity.INTENT_BOOK_NAME, bookName);
                intent.putExtra(DetailActivity.INTENT_BOOK_IMAGE_URL, bookImageUrl);
                intent.putExtra(DetailActivity.INTENT_BOOK_DESCRIPTION, bookDescription);

                // Lanza DetailActivity con los datos correspondientes
                context.startActivity(intent);
            }
        });
    }

    // showData asigna los datos recibidos a cada view
    public void showData(BookData data, Activity activity){
        // Guarda en book los datos recibidos
        this.book = data;

        // Asigna al textView el titulo recibido y carga la imagen de la url con glide
        textView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getUrl()).into(imageView);
    }
}
