import org.apache.spark.SparkConf
import org.apache.spark.SparkContext


object SparkContextInitializer {
 val sparkConf = new SparkConf()
    .setAppName("NOUS Graph Pattern Miner")
    .set("spark.rdd.compress", "true")
    .set("spark.shuffle.blockTransferService", "nio")
    .set("spark.serializer",
      "org.apache.spark.serializer.KryoSerializer")
      .setMaster("local")
    

  sparkConf.registerKryoClasses( Array.empty )
  val sc = new SparkContext( sparkConf )
}