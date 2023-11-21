package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.media.Image;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.squareup.picasso.Picasso;

public class DetailActivity extends AppCompatActivity {
    public static final String INTENT_BOOK_NAME = "BOOK_NAME";
    public static final String INTENT_BOOK_IMAGE_URL = "BOOK_IMAGE_URL";
    public static final String INTENT_BOOK_DESCRIPTION = "BOOK_DESCRIPTION";
    private TextView nameTextView;
    private TextView descTextView;
    private ImageView imageView;
    private Activity activity = this;
    private Context context = this;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        Intent intent = getIntent();
        String bookName = intent.getStringExtra(DetailActivity.INTENT_BOOK_NAME);
        String bookImageUrl = intent.getStringExtra(DetailActivity.INTENT_BOOK_IMAGE_URL);
        String bookDescription = intent.getStringExtra(DetailActivity.INTENT_BOOK_DESCRIPTION);

        nameTextView = findViewById(R.id.detail_title);
        nameTextView.setText(bookName);
        imageView = findViewById(R.id.detail_image);
        Picasso.get().load(bookImageUrl).into(imageView);
        descTextView = findViewById(R.id.detail_description);
        descTextView.setText(bookDescription);
    }
}
