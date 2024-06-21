package com.example.springtest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.DependsOn;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

@Component
public class ContentLocaliser {

    @Resource(
        name = "localeGroupMap"
    )
    // private Map<String, List<String>> localeGroupMap;
    private final Map<String, List<String>> localeGroupMap;

    @Autowired
    public ContentLocaliser(@Qualifier("localeGroupMap") Map<String, List<String>> localeGroupMap) {
        this.localeGroupMap = localeGroupMap;
    }
}
