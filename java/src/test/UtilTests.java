package test;

import main.util;
import org.junit.jupiter.api.Assertions;

import java.util.HashMap;

// replace with .assertEquals; * is bad practice in py at least
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class UtilTests {

    HashMap<Integer, Boolean> primeTests = new HashMap<>() {{
        put(-1, false);
        put(1, false);
        put(2, true);
        put(5, true);
        put(8, false);
        put(9, false);
        put(37, true);
        put(251, true);
        put(739, true);
        put(2503, true);
        put(7867, true);
        put(115249, true);
        put(115251, false);
    }};

    @Test
    @DisplayName("util.isPrime Test")
    public void isPrimeTest() {
        primeTests.forEach((key, value) ->
                Assertions.assertEquals(primeTests.get(key), util.isPrime(key)));
    }


}
