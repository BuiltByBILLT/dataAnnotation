package com.example.springtest;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Configuration
public class YourSpringConfiguration {
    @Bean(name = "localeGroupMap")
	public Map<String, List<String>> localeGroupMap() {
		Map<String, List<String>> groupMap = new HashMap<>();
		groupMap.put("APAC", Arrays.asList("AXJ", "AU", "CN", "HK", "IN", "JP", "KO", "MY", "PH", "SG", "TW"));
		groupMap.put("EMEA", Arrays.asList("AE", "AT", "BE", "CH", "DA", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "JE", "GR", "IL", "IM", "IT", "LU", "NL", "NO", "SCOT", "SE", "SK", "ZA"));
		groupMap.put("AMER", Arrays.asList("US", "BR", "CA", "CL", "CO", "MX"));
		return groupMap;
	}
}
