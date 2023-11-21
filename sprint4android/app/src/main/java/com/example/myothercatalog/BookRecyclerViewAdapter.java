package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class BookRecyclerViewAdapter extends RecyclerView.Adapter<BookViewHolder> {
    private List<BookData> allData;
    private Activity activity;

    public BookRecyclerViewAdapter(List<BookData> dataSet, Activity activity){
        this.allData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    public BookViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.book_recycler_cell, parent, false);
        BookViewHolder bookViewHolder = new BookViewHolder(view);
        return bookViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull BookViewHolder holder, int position) {
        BookData dataInPositionToBeRendered = allData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    public int getItemCount() {
        return allData.size();
    }
}
