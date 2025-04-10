package com.esprit.microservice.microservice;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Map;

@Service
public class YoutubeService {

    private final String API_KEY = "AIzaSyC6VJZaT0FsSyg1VVCtxiI_Ml4SnDCjLK8";
    private final String BASE_URL = "https://www.googleapis.com/youtube/v3/search";

    public Map searchVideos(String query) {
        String encodedQuery = URLEncoder.encode(query, StandardCharsets.UTF_8);
        String url = BASE_URL +
                "?part=snippet" +
                "&q=" + encodedQuery +
                "&type=video" +
                "&maxResults=5" +
                "&key=" + API_KEY;

        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.getForObject(url, Map.class);
    }
}
