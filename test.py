import timeit, argparse

def run(test_image_path,model_path): ##TODO
    """
    Run a test for wazer labeling in input image
    :param test_image_path: path to input image location 'image.jpg'
    :param model_path: path to the model
    :return: returns wazer if there is a wazer or empty string otherwise
    """
    result = False

    return 'wazer' if result else ''



if __name__ == '__main__':
    ## parse input arguments: test image, model
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_image_path", type=str, default='image.jpg', help="test image path")
    parser.add_argument("--model_path", type=str, default='model.pb', help="model path")
    opt = parser.parse_args()

    #run test
    start = timeit.default_timer()
    result = run(opt.test_image_path,opt.model_path)
    stop = timeit.default_timer()

    #print results
    print('{} - {}'.format(opt.test_image_path,result))
    print('Run Time: ', stop - start)