package com.example.marketplacepi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication

public class MarketplacePiApplication {

	public static void main(String[] args) {
		SpringApplication.run(MarketplacePiApplication.class, args);
	}

}
