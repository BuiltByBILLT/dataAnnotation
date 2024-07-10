package quickml.supervised.parametricModels;

import com.google.common.collect.Lists;
import it.unimi.dsi.fastutil.ints.Int2DoubleMap;
import it.unimi.dsi.fastutil.ints.Int2DoubleOpenHashMap;
import org.javatuples.Pair;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import quickml.data.instances.SparseRegressionInstance;

import java.io.Serializable;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import static quickml.MathUtils.cappedlogBase2;
import static quickml.MathUtils.sigmoid;

public class ParallelizedLogisticDerivative implements OptimizableCostFunction<SparseRegressionInstance> {

    private int executorThreadCount = Runtime.getRuntime().availableProcessors();
    private ExecutorService executorService=Executors.newFixedThreadPool(executorThreadCount);


    public static final String EXPECTED_FRACTION_OF_FEATURES_TO_UPDATE_PER_WORKER = "expectedFractionOfFeaturesToUpdatePerWorker";
    public static final String EXECUTOR_THREAD_COUNT = "executorThreadCount";
    public static final String MIN_INSTANCES_FOR_PARELLIZATION = "minInstancesForParrellization";
    public static final String SPARSE_PARELLIZATION = "sparseParallelization";
    public static final String OPTIMIZABLE_COST_FUNCTION = "optimizableCostFunction";
    public static final String MAX_GRADIENT_NORM = "maxGradientNorm";
    public static final String RIDGE = "ridge";
    public static final String LASSO = "lasso";

    double ridge = 0;
    double lasso = 0;
    private double expectedFractionOfFeaturesToUpdatePerWorker = 1.0;
    private int minInstancesForParrellization = 100;
    private boolean sparseParallelization = true;
    private double maxGradientNorm = Double.MAX_VALUE;


    private static final Logger logger = LoggerFactory.getLogger(ParallelizedLogisticDerivative.class);

    public ParallelizedLogisticDerivative executorThreadCount(int executorThreadCount);
    public ParallelizedLogisticDerivative maxGradientNorm(double maxGradientNorm)
    public ParallelizedLogisticDerivative minInstancesForParrellization(int minInstancesForParrellization)

    public ParallelizedLogisticDerivative expectedFractionOfFeaturesToUpdatePerWorker(double expectedFractionOfFeaturesToUpdatePerWorker)

    public ParallelizedLogisticDerivative sparseParallelization(boolean sparseParallelization);

    public ParallelizedLogisticDerivative ridgeRegularizationConstant(final double ridgeRegularizationConstant);

    public ParallelizedLogisticDerivative lassoRegularizationConstant(final double ridgeRegularizationConstant);

    public static double probabilityOfTheNegativeClass(double[] weights, SparseRegressionInstance instance);

    public static double probabilityOfThePositiveClass(double[] weights, SparseRegressionInstance instance);

    public void updateBuilderConfig(final Map<String, Serializable> config);

    @Override
    public  double computeCost(List<? extends SparseRegressionInstance> instances, double[] weights, double minPredictedProbablity);

    // This function should compute the gradient, add in the regularization term, and then normalize. It should use sparse computations iff
    // the sparseParallelization flag has been set.
    @Override
    public void updateGradient(final List<? extends SparseRegressionInstance> sparseClassifierInstances, final double[] fixedWeights, final double[] gradient) {
        int currentMiniBatchSize = sparseClassifierInstances.size();
        final int[] threadStartAndStopIndices = getThreadStartIndices(currentMiniBatchSize, executorThreadCount, minInstancesForParrellization);
        int actualNumThreads = threadStartAndStopIndices.length - 1;
        <WRITE YOUR CODE HERE>
    }



    private  void sparseCalculationOfGradient(final List<? extends SparseRegressionInstance> sparseClassifierInstances, final double[] fixedWeights, double[] gradient, final int[] threadStartAndStopIndices, int actualNumThreads);

    private void nonSparseCalculationOfGradient(final List<? extends SparseRegressionInstance> sparseClassifierInstances, final double[] fixedWeights, double[] gradient, final int[] threadStartAndStopIndices, int actualNumThreads);


    static void sparseUpdateUnnormalizedGradientForInstance(double[] weights, Int2DoubleOpenHashMap contributionsToTheGradient,
                                                            SparseRegressionInstance instance);

    private static double gradientContributionOfAFeatureValue(double label, double postiveClassProbability, double value);

    static void updateUnnormalizedGradientForInstance(double[] weights, double[] contributionsToTheGradient,
                                                      SparseRegressionInstance instance);

    public  Int2DoubleOpenHashMap getSparseWorkerContributionToTheGradient(List<? extends SparseRegressionInstance> instances, double[] weights, double expectedFractionOfFeaturesToUpdate);

    public static void addSparseContribution(double[] gradient, Future<Int2DoubleOpenHashMap> contributionFuture);

    public static double[] getWorkerContributionToTheGradient(List<? extends SparseRegressionInstance> instances, double[] weights);

    public static void  reductionToTheGradient(double[] gradient, List<Future<double[]>> contributions);

    public static void addRegularizationComponentOfTheGradient(double[] weights, double[] gradient, double ridge, double lasso);


    public static void addContribution(double[] gradient, Future<double[]> contributionFuture);


    public static double getRegularizationCost(double[] weights, double ridge, double lasso);


    public static void normalizeTheGradient(int minibatchSize, double maxGradientNorm, double[] gradient);


    public static void applyMaxGradientNorm(double maxGradientNorm, double[] gradient);

    public  int[] getThreadStartIndices(int numInstances, int actualNumThreads, int minInstancesForParrallization);

    @Override
    public void shutdown();
}