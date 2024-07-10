package quickml.supervised.parametricModels;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class ParallelizedLogisticDerivativeTest {

    @Test
    public void testInstantiation() {
        ParallelizedLogisticDerivative derivative = new ParallelizedLogisticDerivative();
        assertNotNull(derivative);
    }
}
