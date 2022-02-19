package se.mbaeumer.springboot.log4j;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {

    private static final Logger log = LogManager.getLogger();

    @PostMapping("/post")
    public void someMagicEndpoint(@RequestBody final String name){
        log.info(name);
    }
}
