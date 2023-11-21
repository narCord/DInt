package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class BookData {
    private String name;
    private String url;
    private String description;

    public BookData(JSONObject json) throws JSONException{
        this.name = json.getString("name");
        this.url = json.getString("image_url");
        this.description = json.getString("description");
    }

    public String getName() { return name; }
    public String getUrl() {
        return url;
    }
    public String getDescription() { return description; }
}
