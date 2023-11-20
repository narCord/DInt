package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class BookViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    public BookViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = itemView.findViewById(R.id.book_text_view);
        imageView = itemView.findViewById(R.id.book_image_view);
    }

    public void showData(BookData data, Activity activity){
        textView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getUrl()).into(imageView);
    }
}
